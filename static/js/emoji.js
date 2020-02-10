/**
 emoji_unicode.json data from
 https://github.com/jollygoodcode/twemoji/blob/760af1fc6ce51f452595052630e6a1a666a0ec33/lib/twemoji/data/emoji-unicode.yml
*/

function convert_emoji() {
    let body = document.body;
    let s = body.innerHTML;
    // var s = ":joy: :smile: :grin:"; // body.innerHTML;
    // console.log(s.match(/:[\w-]+:/g));
    body.innerHTML = s.replace(/:[\w-]+?:/g, x => twemoji.convert.fromCodePoint(emoji_unicode[x]));
    twemoji.parse(body);
}
