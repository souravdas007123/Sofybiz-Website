document.addEventListener('DOMContentLoaded', () => {
    let index = 0;
    const slides = document.querySelectorAll('.images');
    const total = slides.length;

    // Show the first image and update content initially
    slides[index].classList.add('active');
    updateContent(index);

    // Event listener for the next button (right arrow)
    document.getElementById('change-1').addEventListener('click', () => {
        changeImage(index + 1);  // Move to next slide
        console.log("Next button clicked");
    });

    // Event listener for the previous button (left arrow)
    document.getElementById('change-2').addEventListener('click', () => {
        changeImage(index - 1);  // Move to previous slide
        console.log("Previous button clicked");
    });

    // Function to change the active image
    function changeImage(newIndex) {
        // Remove 'active' class from the current image
        slides[index].classList.remove('active');

        // Update the index, looping around if necessary
        index = (newIndex + total) % total;  // Ensure it wraps around correctly

        // Add 'active' class to the new image
        slides[index].classList.add('active');

        // Update the content (text data) based on the new active image
        updateContent(index);
    }

    // Function to update the content in .project_gallery_data based on the active image
    function updateContent(index) {
        const activeImage = slides[index];
        const subhead = activeImage.getAttribute('data-subhead');
        const head = activeImage.getAttribute('data-head');
        const para = activeImage.getAttribute('data-para');

        // Update the text content in the project_gallery_data section
        document.getElementById('data-subhead').textContent = subhead;
        document.getElementById('data-head').textContent = head;
        document.getElementById('data-para').textContent = para;
    }
});

