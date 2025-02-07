// Animation for the project section
// The animation will fire on clicking the search button
// This animation contains the movement of the paragraph div respectively

const btn = document.getElementById("src")
let counter = 0;
btn.addEventListener("click", (e)=> {
    e.preventDefault();
    counter++
    const gallery = document.getElementById("gallery_data")
    const image = document.getElementById("image")
    if (counter % 2 != 0){
        gallery.style.transform= 'translateX(-200px)'
        gallery.style.transition = '0.6s'
    }
    else {
        gallery.style.transform = 'translateX(0px)'
        gallery.style.transition = '0.6s'
    }
})

// Project section animation ends here


// counter function for reloading numbers inside company milestone div
// This function will fire when the section comes first time inside the viewport
// Function targets the element having class name count and changes the value to the desired data-target


const speed = 200;

// Function to update the counter
function upDate(count) {
    const target = Number(count.getAttribute("data-target"));
    let counter = 0; // Ensure the counter starts at 0

    // Update counter at an interval
    const interval = setInterval(() => {
        const inc = target / speed;
        counter = counter + inc; // Increment counter by inc
        if (counter < target) {
            count.innerText = Math.floor(counter);
        } else {
            count.innerText = target;
            clearInterval(interval); // Stop the interval when the target is reached
        }
    }, 15);
}

// IntersectionObserver options
const observerOptions = {
    root: null, // Observing in relation to the viewport
    rootMargin: "0px",
    threshold: 0.1 // Trigger when 10% of the section is visible
};

// IntersectionObserver callback
const observerCallback = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // When the section is in view, run the upDate function for each .count in the section
            entry.target.querySelectorAll(".count").forEach(count => {
                upDate(count);
            });
            observer.unobserve(entry.target); // Stop observing this section after it has been triggered
        }
    });
};

// Initialize observer for different sections with different class names
const sectionClasses = [
    ".achivement_wrraper", // Class for section 1
    ".company_wrapper", // Class for section 2
];

// For each section class, initialize an observer
sectionClasses.forEach(sectionClass => {
    const sections = document.querySelectorAll(sectionClass); // Get all sections with the current class
    sections.forEach(section => {
        const observer = new IntersectionObserver(observerCallback, observerOptions);
        observer.observe(section); // Observe each section individually
    });
});

// Counter function for the company section and textimorial section ends here


// Automatic scrolling carousel for contact section
// This function fires whenever the screen width changes to mobile screens


document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.carousel');
    const scrollSpeed = 3; // Speed at which the carousel scrolls, based on item width
    const scrollInterval = 2000; // Interval between scroll actions in milliseconds

    const items = document.querySelectorAll('.link');
    const itemWidth = items[0].offsetWidth; // Get the width of a single item

    let scrollAmount = 0;

    function scrollCarousel() {
        if (scrollAmount < carousel.scrollWidth - carousel.offsetWidth) {
            // Scroll to the next item
            scrollAmount += itemWidth;
        } else {
            // Reset to the beginning once the end is reached
            scrollAmount = 0;
        }

        // Scroll horizontally with smooth behavior
        carousel.scrollTo({
            left: scrollAmount,
            behavior: 'smooth',
        });
    }

    // Set an interval to automatically scroll the carousel horizontally
    setInterval(scrollCarousel, scrollInterval);
});

// Contact section javascript ends here


// Automatic zoom-in slider sliding elements inside the textimorial wrapper
// This function also fires whenever the section comes inside the viewport
// It contains an additional zoom-in and zoom-out effect for better experience

const items = document.querySelectorAll('.textimorial_details_wrraper');//.textimorial_details_wrraper
const totalItems = items.length;
let currentIndex = 0; // To keep track of the current item
const scrollSpeed = 2000; // Duration for one full scroll cycle (in ms)

// Initialize items in the center
function initializeItems() {
  items.forEach((item, index) => {
    // Set initial position of items to start at the center
    const offset = (index - currentIndex) * 100; // 100% width for each item
    item.style.transform = `translateX(${offset}%)`;

    // Apply zoom effect for the centered item
    if (offset === 0) {
      item.style.transform += ' scale(1.1)'; // Zoom-in effect for the centered item
    } else {
      item.style.transform += ' scale(0.4)'; // Reset zoom for non-centered items
    }
  });
}

// Function to move items
function moveItems() {
  // Move each item to its new position
  items.forEach((item, index) => {
    const offset = (index - currentIndex) * 100; // 100% for each item
    item.style.transform = `translateX(${offset}%)`;

    // Apply zoom effect (scale) based on the position of the item
    if (offset === 0) { // If the item is centered
      item.style.transform += ' scale(1.2)'; // Zoom-in effect
    } else {
      item.style.transform += ' scale(1)'; // Reset zoom-out effect
    }
  });

  // Move to the next item
  currentIndex = (currentIndex + 1) % totalItems; // Loop back to the first item when reaching the end
}

// Start the movement loop
setInterval(moveItems, scrollSpeed);

// Initialize positions and zoom effect
initializeItems();

// Textimorial section javascript ends here


// Function for animation on the images of all the section that are not being animated yet
// This function makes the image fadi-in and fade-out whenever the image is inside the viewport


const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Add fade-in class when image is in the viewport
        entry.target.classList.add('fade-in');
      } else {
        // Remove fade-in class when image is out of the viewport
        entry.target.classList.remove('fade-in');
      }
    });
  }, {
    threshold: 0.5 // Image must be 50% in the viewport to trigger the fade-in
  });

  // Observe all images with the 'fade-image' class
  const images = document.querySelectorAll('.fade-image');
  images.forEach(image => observer.observe(image));

// Image animation javascript ends here




// Landing image slider function for sliding images through button click

let currentImageIndex = 0;
const pics = document.querySelectorAll('.screen');
const totalImages = pics.length;

console.log(pics)
// Show the first image initially
pics[currentImageIndex].style.display = 'block';

document.getElementById('nextBtn').addEventListener('click', () => {
    showImage(currentImageIndex + 1);
    console.log("clicked")
});

document.getElementById('prevBtn').addEventListener('click', () => {
    showImage(currentImageIndex - 1);
    console.log("clicked again")
});

function showImage(index) {
    // Hide the current image
    pics[currentImageIndex].style.display = 'none';

    // Adjust the new index, looping around
    currentImageIndex = (index + totalImages) % totalImages;

    // Show the new image
    pics[currentImageIndex].style.display = 'block';
}


// Project image slider function for sliding images through button click

// let Index = 0;
// const slides = document.querySelectorAll('.images');
// const total = slides.length;

// console.log(slides)
// // Show the first image initially
// slides[Index].style.display = 'block';

// document.getElementById('change-2').addEventListener('click', () => {
//     showImage(Index + 1);
// });

// document.getElementById('change-1').addEventListener('click', () => {
//     showImage(Index - 1);
// });

// function showImage(index) {
//     // Hide the current image
//     slides[Index].style.display = 'none';

//     // Adjust the new index, looping around
//     Index = (index + total) % total;

//     // Show the new image
//     slides[Index].style.display = 'block';
// }
