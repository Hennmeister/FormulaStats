let open = false;

function showDrivers() {
    document.getElementById("myDropdown").classList.add("show");
    open = true;
}

function closeSearch() {
    console.log(open);
    document.getElementById("myDropdown").classList.remove("show");
    if (open){
        document.getElementById("myDropdown").classList.add("show");
        open = false;
    }
    open = false;
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("searchBox");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().slice(0, filter.length) == filter) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
