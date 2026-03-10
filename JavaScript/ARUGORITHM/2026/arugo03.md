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

[エラトステネスの篩](https://algo-method.com/descriptions/64)

## 行った理由

素数計算のアルゴリズム書いたことあった
この書き方書いたことなかった

### 点数と合否
85/100
合格

自分のコード
```
function Eratosthenes(number) {
    const isprime = new Array(number + 1);
    const newIsprime = isprime.fill(true);
    newIsprime[0] = false;
    newIsprime[1] = false;

    for (let i = 2; i <= number; i++) {
        if (!newIsprime[i]) {
            continue;
        }

        let q = i * 2

        while (q <= number) {
            newIsprime[q] = false;
            q += i
        }
    }
    return newIsprime;
}

console.log(Eratosthenes(50));
```



AI添削後
```
function Eratosthenes(number) {
    // numberの桁確認
    if (number > 10000000) {
        throw new Error("numberが大きすぎます")
    }

    // 変数の冗長さ (-5点) 変数を分ける必要がない
    // const isprime = new Array(number + 1);
    // const newIsprime = isprime.fill(true);

    const isprime = new Array(number + 1).fill(true);

    newIsprime[0] = false;
    newIsprime[1] = false;

    for (let i = 2; i <= number; i++) {
        if (!newIsprime[i]) {
            continue;
        }

        // `q`の初期値が非効率 (-10点)
        // let q = i * 2　// i = 5 のとき　q = 10 から始まる
        let q = i * i; // i = 5 のとき　q = 25から始まる(それ以前は処理済みのため 10は2の倍数なのでそこでfalseになっている)

        while (q <= number) {
            newIsprime[q] = false;
            q += i
        }
    }
    return newIsprime;
}

console.log(Eratosthenes(50));
```

[回文かどうか](https://algo-method.com/tasks/227)

```
function Main(input) {
    const word = input.trim().split("");

    if (word.join("") === word.reverse().join("")) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));

```

[カードの並べ替え（1）](https://algo-method.com/tasks/9d11ed34c8156caa)
```
function Main(input) {
    const word = input.trim().split(" ");

    const count = word[0];
    const arr = []
    for (let i = 0; i <= count - 1; i++) {
        arr[i] = i
    }
    const splice = arr.splice(word[1], word[2] - (word[1] - 1))

    console.log(...splice,...arr);
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));

```
