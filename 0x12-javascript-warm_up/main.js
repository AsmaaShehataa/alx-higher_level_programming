const myImage = document.querySelector('img');
myImage.onclick = () => {
  const mySrc = myImage.getAttribute('src');
  if (mySrc === 'images/google-icon.png') {
    myImage.setAttribute('src', 'images/google-icon.png');
  } else {
    myImage.setAttribute('src', 'images/google-icon.png');
  }
};
