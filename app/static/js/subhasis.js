//NavBar
function showDropdown() {
  document.getElementById("dropdownMenu").style.display = "block";
}

function hideDropdown() {
  document.getElementById("dropdownMenu").style.display = "none";
}

//NavBar
//Product Section
$('.owl-carousel-Product').owlCarousel({
  loop: true,
  margin: 10,
  nav: false,
  dots: false,
  autoplay: true,
  smartSpeed: 3000,
  // autoplayTimeout: 3000,
  autoplayHoverPause: true,
  responsive: {
      0: {
          items: 1
      },
      360: {
          items: 1.9
      },
      550: {
          items: 2.5
      },
      750: {
          items: 3.5
      },
      850: {
          items: 4
      },
      950: {
          items: 4.5
      },
      1150: {
          items: 5.5
      }
  }
})

// For ProductName
document.addEventListener("DOMContentLoaded", function () {
  var ProductNames = document.querySelectorAll(".ProductName");
  ProductNames.forEach(function (ProductName) {

      var originalText = ProductName.innerHTML;
      var maxLength = 52;
      var originalLength = originalText.length;
      console.log(originalLength);
      if (originalLength > maxLength) {
          console.log(originalText.length);
          var truncatedText = originalText.slice(0, 52) + "...";
          ProductName.textContent = truncatedText;
      }
  });

});

//Brand Carousel
$('.vendor-carousel').owlCarousel({
  loop: true,
  margin: 10,
  nav: false,
  dots: false,
  autoplay: true,
  smartSpeed: 3000,
  responsive: {
      0: {
          items: 2.5
      },
      576: {
          items: 3.5
      },
      700: {
          items: 4.5
      },
      768: {
          items: 5.5
      },
      992: {
          items: 6.5
      },
      1200: {
          items: 7.5
      }
  }
});

var MonitorProduct = document.getElementById("MonitorProduct");
var BestSellingProduct = document.getElementById("BestSellingProduct");
var LaptopProduct = document.getElementById("LaptopProduct");

function showProductCarousel(productToShow, filterClass) {
  // Hide all products
  MonitorProduct.style.display = "none";
  BestSellingProduct.style.display = "none";
  LaptopProduct.style.display = "none";

  // Show the selected product
  productToShow.style.display = "block";

  // Remove 'active' class from all filters
  var allProductType = document.querySelectorAll('.ProductCategory');
  allProductType.forEach(filter => {
      filter.classList.remove('active');
  });

  // Add 'active' class to the selected filter
  var activeFilter = document.querySelector('[data-filter="' + filterClass + '"]');
  activeFilter.classList.add('active');
}

document.getElementById("MonitorFilter").addEventListener("click", function () {
  showProductCarousel(MonitorProduct, ".filter-Monitor");
});

document.getElementById("LaptopFilter").addEventListener("click", function () {
  showProductCarousel(LaptopProduct, ".filter-Laptop");
});

document.getElementById("BestSellingFilter").addEventListener("click", function () {
  showProductCarousel(BestSellingProduct, ".filter-BestSelling");
});
//For Product carousel End

// For ScrollBar
function scrollToTop() {
  window.scrollTo({
      top: 0,
      behavior: 'smooth'
  });
}

let scrollDiv = document.getElementById("scrollDiv");
window.onscroll = function () {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      scrollDiv.style.display = "block";

  } else {
      scrollDiv.style.display = "none";
  }
};

// ScrollBar End