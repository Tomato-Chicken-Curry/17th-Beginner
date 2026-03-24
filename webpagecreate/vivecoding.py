<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Daily Tracker</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #667eea, #764ba2);
      margin: 0;
      color: #333;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .container {
      background: white;
      padding: 30px;
      border-radius: 20px;
      width: 350px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }

    h1 {
      text-align: center;
    }

    input {
      width: 70%;
      padding: 10px;
      border-radius: 10px;
      border: 1px solid #ddd;
    }

    button {
      padding: 10px;
      border: none;
      border-radius: 10px;
      background: #667eea;
      color: white;
      cursor: pointer;
    }

    ul {
      list-style: none;
      padding: 0;
    }

    li {
      display: flex;
      justify-content: space-between;
      margin: 10px 0;
      padding: 10px;
      border-radius: 10px;
      background: #f3f3f3;
    }

    .done {
      text-decoration: line-through;
      color: gray;
    }

    .progress {
      margin-top: 15px;
      height: 10px;
      background: #eee;
      border-radius: 10px;
      overflow: hidden;
    }

    .bar {
      height: 100%;
      background: #667eea;
      width: 0%;
    }
  </style>
</head>
<body>

<div class="container">
  <h1>Daily Tracker</h1>

  <div>
    <input type="text" id="todoInput" placeholder="할 일 입력">
    <button onclick="addTodo()">추가</button>
  </div>

  <ul id="todoList"></ul>

  <div class="progress">
    <div class="bar" id="progressBar"></div>
  </div>
</div>

<script>
  let todos = JSON.parse(localStorage.getItem("todos")) || [];

  function save() {
    localStorage.setItem("todos", JSON.stringify(todos));
  }

  function render() {
    const list = document.getElementById("todoList");
    list.innerHTML = "";

    let doneCount = 0;

    todos.forEach((todo, index) => {
      const li = document.createElement("li");

      const span = document.createElement("span");
      span.innerText = todo.text;
      if (todo.done) {
        span.classList.add("done");
        doneCount++;
      }

      span.onclick = () => {
        todos[index].done = !todos[index].done;
        save();
        render();
      };

      const delBtn = document.createElement("button");
      delBtn.innerText = "삭제";
      delBtn.onclick = () => {
        todos.splice(index, 1);
        save();
        render();
      };

      li.appendChild(span);
      li.appendChild(delBtn);
      list.appendChild(li);
    });

    const percent = todos.length ? (doneCount / todos.length) * 100 : 0;
    document.getElementById("progressBar").style.width = percent + "%";
  }

  function addTodo() {
    const input = document.getElementById("todoInput");
    if (!input.value) return;

    todos.push({ text: input.value, done: false });
    input.value = "";

    save();
    render();
  }

  render();
</script>

</body>
</html>
