[成績判定（7）](https://algo-method.com/tasks/3c5f9db3a7dd3e75)

function Main(input) {
  const str = input.trim().split("\n");

  let count = str[0];
  for (let i = 1; i <= count; i++) {
    const [A, B] = str[i].trim().split(" ");
    const value = (Number(A) + Number(B)) / 2;
    const val = value > B
      ? value
      : B;
    if (val >= 90) {
        console.log("S");
    } else if (val < 90 && val >= 80) {
        console.log("A");
    } else if (val < 80 && val >= 70) {
        console.log("B");
    } else if (val < 70 && val >= 60) {
        console.log("C");
    } else if (val < 60) {
        console.log("F");
    }
  }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
