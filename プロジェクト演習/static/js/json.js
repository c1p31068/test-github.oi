function setImage(e) {
  const file = e.target.files;
  const reader = new FileReader();
  reader.readAsDataURL(file[0]);
  reader.onload = () => {
    const image = document.getElementById('img');
    image.src = reader.result;
  };
}
