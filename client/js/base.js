'use strict';

global.jQuery = require("jquery");
global.Tether = require("tether");
                require('bootstrap');

// Bootstrap Tooltip Init
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});
