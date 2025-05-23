function simplifyPath(path: string): string {
    let stack: string[] = path.split("/");
    stack = stack.filter((v) => v != "");

    let len = stack.length;

    let i = 0;
    while (i < len) {
        let cur = stack[i];

        if (cur == ".") {
            stack.splice(i, 1);
            len--;
        } else if (cur == "..") {
            if (i == 0) {
                stack.splice(i, 1);
                i = 0;
                continue;
            }

            stack.splice(i - 1, 2);
            i--;
            len--;
        } else {
            i++;
        }

        if (stack.length == 1) {
            break;
        }
    }

    let res = "/";
    stack.forEach((v, i) => {
        if (i == stack.length - 1) {
            res += v;
        } else {
            res += v + "/";
        }
    });

    return res;
}

console.log(simplifyPath("/a/../../b/../c//.//"));
