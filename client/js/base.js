'use strict';

global.jQuery = require('jquery');
global.Tether = require('tether');
                require('bootstrap');

// Bootstrap Tooltip Init
jQuery(function () {
  jQuery('[data-toggle="tooltip"]').tooltip()
});
