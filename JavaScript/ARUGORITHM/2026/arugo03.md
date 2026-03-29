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

[カードの並べ替え（2）](https://algo-method.com/tasks/59b21a013d03f7f6)
```
function Main(input) {
    const number =JSON.parse(input.trim());
    const arr = Array.from({ length: number * 2}, (_, i) => i);
    for (let i = number; i > 0; i--) {
        console.log(arr.shift());
        console.log(arr.pop());
    }

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

[できるだけ買う](https://algo-method.com/tasks/75444665259feb4b)
```
function Main(input) {
    const word = input.trim().split(" ");
    const num = word[0] / word[1]
    console.log(Math.floor(num));
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```
[何個あまるか](https://algo-method.com/tasks/f4403edd28d0b173)
```
function Main(input) {
    const word = input.trim().split(" ");
    const num = word[0] % word[1]
    console.log(Math.floor(num));
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));

```

[奇数と偶数](https://algo-method.com/tasks/d0e7ccc525dec3cd)
```
function Main(input) {
    const word = input.trim();
    const num = word % 2;
    if (num === 0) {
        console.log("even");
    } else {
        console.log("odd");
    }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));

```

[階段図形](https://algo-method.com/tasks/fc69a3d0589bcc94)
```
function Main() {
    for (let i = 1; i <= 9; i++) {
        const arr = [];
        for (let j = 1; j <= i; j++) {
            arr.push(i)
        }
        console.log(arr.join(""))
    }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

[九九の一覧](https://algo-method.com/tasks/f6c9d310f48b1cbc)
```
for (let i = 1; i <= 9; i++) {
    for (let l = 1; l <= 9; l++) {
        const answer = i * l
        console.log(`${i} * ${l} = ${answer}`);
    }
}
```
[九九表](https://algo-method.com/tasks/26ece8190860645f)
```
for (let i = 1; i <= 9; i++) {
    for (let l = 1; l <= 9; l++) {
        const answer = i * l
        console.log(answer);
    }
    console.log("\n")
}
```

[無駄のない九九](https://algo-method.com/tasks/f8050725813f22a5)

```
for (let i = 1; i <= 9; i++) {
    for (let l = 1; l <= 9; l++) {
        const answer = i * l
        console.log(answer);
    }
    console.log("\n")
}
```

[文字探し（1）](https://algo-method.com/tasks/cc45da0c69d04893)
```
function Main(input) {
  const arr = input.trim().split("\n");
  const str = arr[1].trim().split("");

  for (let i = 0; i <= arr[0]; i++) {
    if (str[i] === "a") {
        console.log(i)
    }
  }

}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```


[データ構造とアルゴリズム]
再帰　p123
```
function countdown(number) {
    console.log(number);

    if (number === 0) {
        return;
    } else {
        countdown(number - 1); //ここで自分自身を呼んでいる
    }
}
```

再帰　p138
採点：85点 / 100点
1. 文字列の配列を受け取り全文字列の総文字数を返す関数を再帰を用いて書きなさい。
```
function Main(input) {
    const arr = JSON.parse(input.trim());

    const countAll = (inputC = arr, index = 0, number = 0) => {
        if (inputC.length !== index) {
            const countA = inputC[index].length;
            return countAll(inputC, index + 1, countA + number)
        } else {
            return number
        }
    }
    const result = countAll();
    console.log(result);
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

リファクタリング
```
function Main(input) {
    const arr =JSON.parse(input.trim());

    const countAll =(arr, index = 0, total = 0) => {
        if (index !== arr.length) {
            return countAll(arr, index + 1, total + arr[index].length);
        } else {
            return total;
        }
    }
    console.log(countAll(arr));
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

再帰　p139
採点：65点 / 100点
再帰の鉄則：再帰関数は引数だけで状態を管理する！外の変数に触らない！
2. 数の配列を受け取って、偶数だけを含む新たな配列を返す関数を再帰を用いて書きなさい。
```
function Main(input) {
    const arr =JSON.parse(input.trim());
    let total = []; // ← 関数の外にある・2回呼ぶと壊れる(console.log(countAll(arr));が同じ階層にあるため)・**副作用**というらしい

    const countAll =(arr, index = 0) => {
        if (arr.length !== index) {
            if (arr[index] % 2 === 0) {
                // ❌ total.push()の戻り値は「配列の新しい長さ（数値）」
                return countAll(arr, index + 1, total.push(arr[index]));
                //                               ^^^^^^^^^^^^^^^^^^^^^^^^^^
                //                               これは [2,4] ではなく 2 (数値) が渡される！
            } else {
                return countAll(arr, index + 1, total);
            }
        } else {
            return total
        }

    }
    console.log(countAll(arr));
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```

リファクタリング
```
function Main(input) {
    const arr =JSON.parse(input.trim());
    let total = [];

    const countAll =(arr, index = 0, total = []) => {
        if (index !== arr.length) {
            if (arr[index] % 2 === 0) {
                // スプレッド構文で新しい配列を作る（元の配列を壊さない）
                return countAll(arr, index + 1, [...total, arr[index]]);
            } else {
                return countAll(arr, index + 1, total);
            }
        } else {
            return total
        }

    }
    console.log(countAll(arr));
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
```
副作用：関数の外の状態を変えること・純粋な関数でなくなる・デバックしにくい(どこで値が変わったのかわからない)・再利用しやすい

純粋関数と副作用の比較
```
// ❌ 副作用あり（純粋でない関数）
let total = [];
const addEven = (arr) => {
    total.push(arr); // 外を変える
};

// ✅ 副作用なし（純粋関数）
const addEven = (arr, total = []) => {
    return [...total, arr]; // 新しい値を返すだけ
};
```
**まとめ**
関数は「引数を受け取り、戻り値を返す」だけにする！
外の変数に触るのは極力避ける！

> この考え方を**「純粋関数（Pure Function）**」と言います。副作用をなくすことで、バグが減り、コードが読みやすくなります
> push() や外部変数への代入を見かけたら、「副作用では？」と疑う癖をつけましょう！

再帰　p139
採点：65点 / 100点
3. 三角数という数列がある。そのパターンは、1, 3, 6, 10, 15, 21で始まり、N番目の数が直前の数にNを足したものである。
