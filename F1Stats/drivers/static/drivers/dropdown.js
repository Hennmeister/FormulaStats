toChange = false;

function showDrivers() {
    dropdown = document.getElementById("dropdown")
    if (!dropdown.classList.contains("show")) {
        dropdown.classList.add("show")
        document.getElementById("searchBox").focus();
        toChange = false;
    }
    else {
        toChange = true;
    }
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("searchBox");
  filter = input.value.toUpperCase();
  div = document.getElementById("dropdown");
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

function deselect() {
    if (toChange && document.getElementById("dropdown").classList.contains("show")) {
        document.getElementById("dropdown").classList.remove("show");
    }
    toChange = !toChange;
}
