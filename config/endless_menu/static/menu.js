const INNER_SUB_MENUS_BTN = document.querySelectorAll(
  ".menu > ul > .menu-item.sub-menu .menu-item.sub-menu > a"
);

const slideUp = (target) => {
  const { parentElement } = target;
  parentElement.classList.remove("open");

};
const slideDown = (target) => {
  const { parentElement } = target;
  parentElement.classList.add("open");

};

const slideToggle = (target) => {
  if (window.getComputedStyle(target).display === "none")
    return slideDown(target);
  return slideUp(target);
};

INNER_SUB_MENUS_BTN.forEach((element) => {
  element.addEventListener("click", () => {
    slideToggle(element.nextElementSibling);
  });
});