// index.html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Page</title>
  </head>
  <body>
    <p id="response"></p>

    <script>
      function sendRequest() {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
          if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("response").innerHTML = xhr.responseText;
          }
        }
        xhr.open("GET", "main_window.py", true);
        xhr.send();
      }

      sendRequest();
    </script>
  </body>
</html>
