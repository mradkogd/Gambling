const slotImages = ['cherry.png', 'lemon.png', 'seven.png'];

const spinButton = document.getElementById('spin-button');
const reels = document.querySelectorAll('.reel');

spinButton.addEventListener('click', () => {
  reels.forEach(reel => {
    const randomIndex = Math.floor(Math.random() * slotImages.length);
    reel.innerHTML = `<img src="${slotImages[randomIndex]}">`;
  });

  const reel1 = reels[0].querySelector('img').src;
  const reel2 = reels[1].querySelector('img').src;
  const reel3 = reels[2].querySelector('img').src;

  if (reel1 === reel2 && reel2 === reel3) {
    window.alert('You won!');
  }
});

