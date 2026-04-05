[一致箇所（1）](https://algo-method.com/tasks/b6fdc32a0850f568)
```
function Main(input) {
  const arr = input.trim().split("\n");
  const str1 = arr[1].trim().split("");
  const str2 = arr[2].trim().split("");
  let count = 0;

  for (let i = 0; i <= arr[0] - 1; i++) {
        if (str1[i] === str2[i]) {
            count += 1;
        }
  }
        console.log(count)

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));

```

[一致箇所（2）] (https://algo-method.com/tasks/dc7657f4c605eaaa)
```
function Main(input) {
  const arr = input.trim().split("\n");
  const str1 = arr[1].trim().split("");
  const str2 = arr[2].trim().split("");
  let count = 0;

  for (let i = 0; i <= arr[0] - 1; i++) {
        if (str1[i] === str2[i] || str1[i] === "?" || str2[i] === "?") {
            count += 1;
        }
  }
        console.log(count)

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

[文字列探し（1）](https://algo-method.com/tasks/dee0750d5d0565a9)
```
function Main(input) {
  const arr = input.trim().split("\n");
  const str1 = arr[1].trim().split("");
  let count = 0;

  for (let i = 0; i <= arr[0] - 1; i++) {
        if (str1[i] === "a" && str1[i + 1] === "b" && str1[i + 2] === "c") {
            count += 1;
        }
  }
        console.log(count)

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```
