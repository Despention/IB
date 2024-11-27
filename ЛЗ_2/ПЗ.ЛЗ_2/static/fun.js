$(".navTrigger").click(function () {
  $(this).toggleClass("active");
  console.log("Clicked menu");
  $("#mainListDiv").toggleClass("show_list");
  $("#mainListDiv").fadeIn();
});

const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

document.addEventListener(
  "click",
  function (event) {
    console.log(event.target.parentElement.parentElement);
    if (
      event.target.parentElement.parentElement.matches(
        ".gallery-image__preview"
      )
    ) {
      event.target.parentElement.parentElement.classList.remove(
        "gallery-image__preview"
      );
      event.target.parentElement.parentElement.scrollIntoView();
    } else if (event.target.matches(".gallery-image__media")) {
      var previewing = document.getElementsByClassName(
        "gallery-image__preview"
      );
      for (el of previewing) {
        el.classList.remove("gallery-image__preview");
      }
      event.target.parentElement.parentElement.classList.add(
        "gallery-image__preview"
      );
      event.target.parentElement.parentElement.scrollIntoView();
    }
  },
  false
);

