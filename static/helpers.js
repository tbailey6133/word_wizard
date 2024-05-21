function getWordDefinition(word) {
  const url = `https://api.dictionaryapi.dev/api/v2/entries/en/${word}`;

  return fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((definition) => {
      if (definition && definition.length > 0) {
        return definition[0]["meanings"][0]["definitions"];
      } else {
        console.log("No definition found");
      }
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
      return { definition: "No definition found." };
    });
}

function showModal(buttonId) {
  const modal = document.getElementById("definitionModal");
  const closeBtn = document.querySelector(".modal-content .close");

  const clickedWord = buttonId.querySelector("span").textContent;

  getWordDefinition(clickedWord)
    .then((definitions) => {
      definitions.forEach((def) => {
        const li = document.createElement("li");
        li.textContent = def.definition;
        modal.querySelector("ol").appendChild(li);
      });
    })
    .catch((err) => {
      const li = document.createElement("li");
      li.textContent = "No definition found";
      modal.querySelector("ol").appendChild(li);

      modal.style.display = "block";
    });
  modal.querySelector("h2").textContent = "";
  modal.querySelector("ol").innerHTML = "";

  modal.querySelector("h2").textContent = clickedWord;

  modal.style.display = "block";

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  window.addEventListener("click", (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });
}

function getAlphanumericChar(char) {
  const code = char.charCodeAt(0);
  return (code > 64 && code < 91) || (code > 96 && code < 123);
}

function getInputValues() {
  return document.querySelectorAll(".hive-cell input");
}

function makeInputValuesArray(inputs) {
  const inputarr = [];

  for (let i = 0; i <= 6; i++) {
    inputarr.push(inputs[i].value.toLowerCase());
  }
  return inputarr;
}

function checkSetForAlphaNumericChars(inputSet) {
  for (let val of inputSet) {
    let alphatest = getAlphanumericChar(val);
    if (!alphatest) {
      return false;
    }
  }
  return true;
}

function checkValidFormSubmit(event) {
  const inputs = getInputValues();
  const inputArr = makeInputValuesArray(inputs);

  const enteredValues = new Set(inputArr);

  if (enteredValues.size < 7) {
    alert("Please include seven unique characters!");
    event.preventDefault();
    location.reload();
  } else {
    const validCharacterCheck = checkSetForAlphaNumericChars(enteredValues);

    if (!validCharacterCheck) {
      alert("Please only include valid characters!");
      event.preventDefault();
      location.reload();
    }
  }
}
