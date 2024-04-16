var ProductImg = document.getElementById("ProductImg");
var SmallImg = document.getElementsByClassName("small-img");
for (var i = 0; i < SmallImg.length; i++) {
    SmallImg[i].onclick = function (event) {
        // Reset opacity for all small images
        for (var j = 0; j < SmallImg.length; j++) {
            SmallImg[j].style.opacity = "0.8";
        }
        // Set opacity of the clicked image to 100%
        event.target.style.opacity = "1";
        // Set the ProductImg src to the clicked image src
        ProductImg.src = event.target.src;
    };
}

// ---------------------------------------------
var cursor = document.querySelector("#cursor");
var images = document.querySelectorAll(".img-container");

document.addEventListener("mousemove", function(event) {
  var x = event.clientX;
  var y = event.clientY;
  cursor.style.left = x + "px";
  cursor.style.top = y + "px";
});

images.forEach(function(image) {
  image.addEventListener("mouseenter", function() {
    cursor.style.display = "block";
  });

  image.addEventListener("mouseleave", function() {
    cursor.style.display = "none";
    image.querySelector("img").style.transform = ""; // Reset image transformation
  });

  image.addEventListener("mousemove", function(event) {
    var rect = image.getBoundingClientRect();
    var offsetX = event.clientX - rect.left;
    var offsetY = event.clientY - rect.top;
    var containerWidth = image.offsetWidth;
    var containerHeight = image.offsetHeight;
    var imageWidth = image.querySelector("img").naturalWidth;
    var imageHeight = image.querySelector("img").naturalHeight;
    var scale = 1.2; // Zoom factor
    var zoomedWidth = imageWidth * scale;
    var zoomedHeight = imageHeight * scale;
    var translateX = (zoomedWidth - containerWidth) / 2;
    var translateY = (zoomedHeight - containerHeight) / 2;
    var backgroundPositionX = -(offsetX * scale - offsetX - translateX);
    var backgroundPositionY = -(offsetY * scale - offsetY - translateY);
    image.querySelector("img").style.transform = `translate(${backgroundPositionX}px, ${backgroundPositionY}px) scale(${scale})`;
  });
});




