function xorDecrypt(data, key) {
  let result = "";
  for (let i = 0; i < data.length; i++) {
    result += String.fromCharCode(
      data.charCodeAt(i) ^ key.charCodeAt(i % key.length)
    );
  }
  return result;
}


const encrypted = [
  36, 0, 15, 22, 29, 4, 11, 18, 17, 31,
  42, 60, 57, 44, 52, 30, 47, 47, 38, 40,
  43, 35, 58, 63, 42, 43, 40, 58, 50, 43,
  47, 49, 54, 61, 49, 62, 42, 34, 60, 38,
  62, 58, 57, 42, 56, 60, 60, 40, 38, 34,
  55, 37, 55, 54, 16
].map(c => String.fromCharCode(c)).join("");

function unlock() {
  const key = document.getElementById("key").value;
  const msg = document.getElementById("msg");

  const decrypted = xorDecrypt(encrypted, key);

  if (decrypted.startsWith("SecurinetsISTIC{")) {
    msg.style.color = "#00ffcc";
    msg.textContent = decrypted;
  } else {
    msg.style.color = "#ff4d4d";
    msg.textContent = "Wrong key";
  }
}
/*
  If you're reading this:
  - Yes, this runs entirely on the client
  - Yes, it can be reversed
  - The key is: "welcome"
*/