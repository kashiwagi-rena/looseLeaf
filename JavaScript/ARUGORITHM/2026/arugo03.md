# アルゴ式

[平均値](https://algo-method.com/tasks/af2699380eaa6ec5)

```
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
```


[反転](https://algo-method.com/tasks/e91bb27bb7976b9b)

```
function Main(input) {
  const str = input.trim().split("\n");
  const quantity = str[0];

  const arr = str[1].trim().split(" ");

  for (let i = quantity - 1; i >= 0 ; i--) {
    console.log(arr[i])
  }

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

[カウントダウン](https://algo-method.com/tasks/b605dcd9e895aad2)

```
function Main(input) {
  for (let i = 9; i >= 0 ; i--) {
    console.log(i + 1)
  }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));

```

[逆から読む](https://algo-method.com/tasks/7968b5c6e82fab73)

```
function Main(input) {
    const word = input.trim().split("");
    const reverse = word.reverse();
    console.log(reverse.join(""));
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```


