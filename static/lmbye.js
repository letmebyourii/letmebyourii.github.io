function showFileName() {
    const fileInput = document.getElementById('file-input');
    const fileNameSpan = document.getElementById('file-name');
  
    if (fileInput.files.length > 0) {
      fileNameSpan.textContent = fileInput.files[0].name;
    }
  }