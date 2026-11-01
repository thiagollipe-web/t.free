// Pure boundary tests, not a substitute for end-to-end browser QA.
const fs=require('node:fs'), vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync('assets/chat.js','utf8');
const fn=source.slice(source.indexOf('function localBase()'),source.indexOf('async function request'));
for(const endpoint of ['http://localhost:11434','http://127.0.0.1:11434','http://[::1]:11434']) {
 const context={URL,$:()=>({value:endpoint})};vm.createContext(context);assert.equal(vm.runInContext(fn+';localBase()',context),endpoint);
}
for(const endpoint of ['https://example.com','http://localhost.evil.example','http://user:secret@localhost:11434','http://localhost:11434/api','http://localhost:11434?key=secret','file:///tmp/model','not-a-url']) {
 const context={URL,$:()=>({value:endpoint})};vm.createContext(context);assert.throws(()=>vm.runInContext(fn+';localBase()',context));
}
console.log('10 endpoint boundary cases passed');
