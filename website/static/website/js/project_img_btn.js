// Project image slider function for sliding images through button click

let Index = 0;
const slides = document.querySelectorAll('.project');
const total = slides.length;

console.log(slides)
// Show the first image initially
slides[Index].style.display = 'block';

document.getElementById('change1').addEventListener('click', () => {
    showImage(Index + 1);
});

document.getElementById('change2').addEventListener('click', () => {
    showImage(Index - 1);
});

function showImage(index) {
    // Hide the current image
    slides[Index].style.display = 'none';

    // Adjust the new index, looping around
    Index = (index + total) % total;

    // Show the new image
    slides[Index].style.display = 'block';
}
