const textEl = document.querySelector("#text-el")

const text =
  "Embark on a learning adventure like never before! At StudyLounge, your journey begins with vibrant discussions, interactive lounges, and a community dedicated to expanding knowledge together.";




  function textTypingEffect(element, text, i = 0) {
    if (i === 0) {
      element.textContent += " ";
    }
    element.textContent += text[i];
 

    if (i === text.length - 1) {
      return;
    }
      setTimeout(() => textTypingEffect(element, text, i + 1), 50);
     
};

  textTypingEffect(textEl, text);


const navEl = document.querySelector("#nav-el")
const navContent = document.querySelector("#nav-content");


navEl.addEventListener('click', function(){
  if (navContent.style.display === 'none') {
    navContent.style.display = 'block'
    navEl.innerHTML = `<i class="fa-solid fa-xmark fa-2xl"></i>`
  }
  else {
    navContent.style.display = 'none'
       navEl.innerHTML = `<i class="fa-solid fa-bars fa-2xl <<<< lg:hidden">`
  }
 
})





function navVisibility() {
  const authNav = document.querySelector("#auth-nav");
  const chevronEl = document.querySelector(".chevron-el");
  if (authNav.style.display === 'none') {
    authNav.style.display = 'block'
    chevronEl.innerHTML = `<i class="fa-solid fa-chevron-up"></i>`;
  } else {
    authNav.style.display = 'none'
    chevronEl.innerHTML = `<i class="fa-solid fa-chevron-down text-gray-200"></i>`;
  }
}


const openModal = document.getElementById("open-modal")
const closeModal = document.getElementById("close-modal");
const modal = document.getElementById("modal")

openModal.addEventListener("click", function(){
  if (modal.style.display === "none") {
    modal.style.display = "block"
  }
  else {
    modal.style.display ="none"
  }
})


closeModal.addEventListener("click", function(){
  if (modal.style.display === "block") {
    modal.style.display = "none";
  } 
});

window.onclick = (e) => {
  if (e.target == modal) {
      modal.style.display = 'none'
  }
}






function checkInput() {
  const inputBtn = document.getElementById("input-el");
  const sendBtn = document.getElementById("send-btn");
  if (inputBtn.value.trim() !== '') {
    sendBtn.style.display = 'block'
  } else {
    sendBtn.style.display = 'none'
  }
}



const launchModal = document.getElementById("launch-modal");
const browseTopicModal = document.getElementById("browse-topic-modal");
const trashModal = document.getElementById("trash-modal")

launchModal.addEventListener('click', () => {
  if (browseTopicModal.style.display === "none") {
    browseTopicModal.style.display = "block";
  } else {
    modal.style.display = "none";
  }

})

trashModal.addEventListener('click', () => {
  if (browseTopicModal.style.display === 'block') {
    browseTopicModal.style.display = 'none'
  }
} )

window.onclick = (e) => {
  if (e.target == browseTopicModal) {
    browseTopicModal.style.display = "none";
  }
}







function startModal() {
  const deleteModal = document.getElementById("delete-modal");
  if (deleteModal.style.display === 'none') {
    deleteModal.style.display = 'block'
  }
}

function closeDeleteModal() {
  const deleteModal = document.getElementById("delete-modal");
  if (deleteModal.style.display === "block") {
    deleteModal.style.display = "none";
  }
}

window.onclick = (e) => {
    const deleteModal = document.getElementById("delete-modal");
  if (e.target == deleteModal) {
    deleteModal.style.display = "none";
  }
};





     