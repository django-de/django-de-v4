#!/usr/bin/env sh

mkdir -p build/css
mkdir -p build/js
mkdir -p build && rm -f build/assets && ln -s ../client/assets build/assets

cat client/scss/base.scss | ./node_modules/.bin/node-sass --include-path client/scss > build/css/base.css
./node_modules/.bin/browserify -t babelify --presets es2015 client/js/base.js > build/js/base.js

