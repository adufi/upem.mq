!function(){"use strict";var e,t={24804:function(e,t,n){var r=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var o=r(n(73609));o.default((function(){o.default('[data-widget="filtered-select"]').each((function(){var e=o.default("#"+this.dataset.filterField),t=o.default(this),n=[];function r(){var r=t.val();t.empty();var a,i=e.val();if(""===i)a=n;else{a=[];for(var u=0;u<n.length;u++)""!==n[u].value&&-1===n[u].filterValue.indexOf(i)||a.push(n[u])}var l=!1;for(u=0;u<a.length;u++){var f=o.default("<option>");f.attr("value",a[u].value),a[u].value===r&&(l=!0),f.text(a[u].label),t.append(f)}l?t.val(r):t.val("")}o.default("option",this).each((function(){var e;e="filterValue"in this.dataset?this.dataset.filterValue.split(","):[],n.push({value:this.value,label:this.label,filterValue:e})})),r(),e.change(r)}))}))},73609:function(e){e.exports=jQuery}},n={};function r(e){var o=n[e];if(void 0!==o)return o.exports;var a=n[e]={id:e,loaded:!1,exports:{}};return t[e].call(a.exports,a,a.exports,r),a.loaded=!0,a.exports}r.m=t,e=[],r.O=function(t,n,o,a){if(!n){var i=1/0;for(f=0;f<e.length;f++){n=e[f][0],o=e[f][1],a=e[f][2];for(var u=!0,l=0;l<n.length;l++)(!1&a||i>=a)&&Object.keys(r.O).every((function(e){return r.O[e](n[l])}))?n.splice(l--,1):(u=!1,a<i&&(i=a));u&&(e.splice(f--,1),t=o())}return t}a=a||0;for(var f=e.length;f>0&&e[f-1][2]>a;f--)e[f]=e[f-1];e[f]=[n,o,a]},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,{a:t}),t},r.d=function(e,t){for(var n in t)r.o(t,n)&&!r.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})},r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),r.hmd=function(e){return(e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.j=4,function(){var e={4:0};r.O.j=function(t){return 0===e[t]};var t=function(t,n){var o,a,i=n[0],u=n[1],l=n[2],f=0;for(o in u)r.o(u,o)&&(r.m[o]=u[o]);if(l)var c=l(r);for(t&&t(n);f<i.length;f++)a=i[f],r.o(e,a)&&e[a]&&e[a][0](),e[i[f]]=0;return r.O(c)},n=self.webpackChunkwagtail=self.webpackChunkwagtail||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))}(),r.O(void 0,[751],(function(){return r(24804)}));var o=r.O(void 0,[751],(function(){return r(90971)}));o=r.O(o)}();
//# sourceMappingURL=filtered-select.js.map