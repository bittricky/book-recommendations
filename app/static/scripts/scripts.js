document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const searchButton = document.getElementById("search-button");
  const recommendationButton = document.getElementById("recommendation-button");
  const booksContainer = document.getElementById("books-container");
  const loadingElement = document.getElementById("loading");
  const noResultsElement = document.getElementById("no-results");

  // Search when Enter key is pressed
  searchInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      searchBooks();
    }
  });

  // Search when search button is clicked
  searchButton.addEventListener("click", searchBooks);

  // Get recommendations when recommendation button is clicked
  recommendationButton.addEventListener("click", fetchRecommendations);

  function searchBooks() {
    const query = searchInput.value.trim();
    if (query === "") {
      return;
    }

    showLoading();
    fetch(`/api/search?query=${encodeURIComponent(query)}`)
      .then((response) => response.json())
      .then((data) => {
        hideLoading();
        displayBooks(data);
      })
      .catch((error) => {
        console.error("Error searching books:", error);
        hideLoading();
        showNoResults();
      });
  }

  function fetchRecommendations() {
    showLoading();
    fetch("/api/recommendations")
      .then((response) => response.json())
      .then((data) => {
        hideLoading();
        displayBooks(data);
      })
      .catch((error) => {
        console.error("Error fetching recommendations:", error);
        hideLoading();
        showNoResults();
      });
  }

  function displayBooks(data) {
    booksContainer.innerHTML = "";

    if (!data.docs || data.docs.length === 0) {
      showNoResults();
      return;
    }

    noResultsElement.classList.add("hidden");

    data.docs.forEach((book) => {
      const coverUrl =
        book.cover_url || "https://via.placeholder.com/180x250?text=No+Cover";
      const authors = book.author_name
        ? book.author_name.join(", ")
        : "Unknown Author";
      const year = book.first_publish_year
        ? book.first_publish_year
        : "Unknown";
      const rating = Math.floor(Math.random() * 2) + 3; // Random rating between 3-5
      const stars = "★".repeat(rating) + "☆".repeat(5 - rating);

      const bookCard = document.createElement("div");
      bookCard.innerHTML = `
        <div class="bg-white rounded-lg shadow overflow-hidden h-full">
          <div class="h-56 bg-cover bg-center bg-gray-200" style="background-image: url('${coverUrl}')"></div>
          <div class="p-4">
            <div class="text-secondary mb-2">${stars}</div>
            <h3 class="font-bold text-gray-800 mb-1 line-clamp-2">${book.title}</h3>
            <p class="text-gray-600 text-sm mb-1 line-clamp-1">${authors}</p>
            <p class="text-gray-500 text-xs">First published: ${year}</p>
          </div>
        </div>
      `;

      booksContainer.appendChild(bookCard);
    });
  }

  function showLoading() {
    loadingElement.classList.remove("hidden");
    noResultsElement.classList.add("hidden");
    booksContainer.innerHTML = "";
  }

  function hideLoading() {
    loadingElement.classList.add("hidden");
  }

  function showNoResults() {
    noResultsElement.classList.remove("hidden");
  }
});
