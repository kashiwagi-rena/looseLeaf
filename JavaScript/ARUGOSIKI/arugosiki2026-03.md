[平均値](https://algo-method.com/tasks/af2699380eaa6ec5)

function Main(input) {
  const str = input.trim().split("\n");

  const count = Number(str[0]);
  const list = str[1].trim().split(" ")
  let number = 0;

  for (let i = 0; i <= count - 1; i++) {
    number += Number(list[i]);
  }
  const answer = number / count
  console.log(Math.floor(answer))
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));


