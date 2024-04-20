// var ProductImg = document.getElementById("ProductImg");
// var SmallImg = document.getElementsByClassName("small-img");
// for (var i = 0; i < SmallImg.length; i++) {
//     SmallImg[i].onclick = function (event) {
//         // Reset opacity for all small images
//         for (var j = 0; j < SmallImg.length; j++) {
//             SmallImg[j].style.opacity = "0.8";
//         }
//         // Set opacity of the clicked image to 100%
//         event.target.style.opacity = "1";
//         // Set the ProductImg src to the clicked image src
//         ProductImg.src = event.target.src;
//     };
// }

// // ---------------------------------------------
// var cursor = document.querySelector("#cursor");
// var images = document.querySelectorAll(".img-container");

// images.forEach(image => {
//   image.addEventListener("mouseenter", () => cursor.style.display = "block");
//   image.addEventListener("mouseleave", () => {
//     cursor.style.display = "none";
//     image.querySelector("img").style.transform = "";
//   });
//   image.addEventListener("mousemove", event => {
//     var rect = image.getBoundingClientRect(),
//         offsetX = event.clientX - rect.left,
//         offsetY = event.clientY - rect.top,
//         scale = 1.2,
//         translateX = (image.offsetWidth * scale - image.offsetWidth) / 2,
//         translateY = (image.offsetHeight * scale - image.offsetHeight) / 2;
//     image.querySelector("img").style.transform = `translate(${-(offsetX * scale - offsetX - translateX)}px, ${-(offsetY * scale - offsetY - translateY)}px) scale(${scale})`;
//     cursor.style.left = event.clientX + "px";
//     cursor.style.top = event.clientY + "px";
//   });
// });
