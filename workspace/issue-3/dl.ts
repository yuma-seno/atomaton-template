const res = await fetch("https://github.com/yuma-seno/atomaton/releases/download/v0.28.0/atomaton-delivery.zip");
const buf = new Uint8Array(await res.arrayBuffer());
await Bun.write("/tmp/atomaton-workspace/atomaton-delivery.zip", buf);
console.log(res.status, buf.byteLength, String.fromCharCode(buf[0]), String.fromCharCode(buf[1]));
