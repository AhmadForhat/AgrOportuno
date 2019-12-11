const bolinhas = document.querySelectorAll(".bolinha")
const imagemSlide = document.querySelectorAll(".slide-home img")

if(bolinhas.length && imagemSlide.length){
  imagemSlide[0].classList.add('ativo');

  function activeTab(index){
      imagemSlide[0].classList.add('none')
      imagemSlide.forEach((section) => {
          section.classList.remove('ativo');
      })
      imagemSlide[index].classList.add('ativo');
  }

  bolinhas.forEach((itemMenu, index) => {
      itemMenu.addEventListener('click', () => {
          activeTab(index);
      });
  });
}