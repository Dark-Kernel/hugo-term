// Function to check if the user has already liked the blog post.
const hasLikedPost = async () => {
  const url = window.location.href;
  const result = await fetch("https://api.aaron.com.es/likes?url=" + encodeURIComponent(url));
  const data = await result.json();
  return data.liked;
};

// Function to send like or unlike request to the API.
const toggleLike = async () => {
  const url = window.location.href;
  const hasLiked = await hasLikedPost();

  if (hasLiked) {
    // If the user has liked the post, send an "unlike" request.
    await fetch("https://api.aaron.com.es/unlike?url=" + encodeURIComponent(url), { method: "POST" });
  } else {
    // If the user has not liked the post, send a "like" request.
    await fetch("https://api.aaron.com.es/like?url=" + encodeURIComponent(url), { method: "POST" });
  }

  // Update the like count.
  const likes = await sendLike();
  const element = document.querySelector(".likes__button");
  element.querySelector(".likes__emoji").innerHTML = `${likes} 👍`;
};

// Function to get the number of likes from the API.
const sendLike = async () => {
  const url = window.location.href;
  const result = await fetch("https://api.aaron.com.es/likes?url=" + encodeURIComponent(url));
  const data = await result.json();
  return data.likes;
};

// Hook the click handler when DOM is ready.
document.addEventListener("DOMContentLoaded", () => {
  const element = document.querySelector(".likes__button");
  if (element) {
    element.addEventListener("click", toggleLike, { once: true });
  }
});

