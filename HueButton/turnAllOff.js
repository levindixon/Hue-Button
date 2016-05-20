"use strict";

var HOSTNAME = "192.168.1.6";
var USERNAME = "IR1YuGO6xjhdoZHiL7GrAxa2cukIWJrHGRyvQDaz";

var Cylon = require("cylon");

Cylon.robot({
  connections: {
    hue: { adaptor: "hue", host: HOSTNAME, username: USERNAME }
  },

  devices: {
    bulb1: { driver: "hue-light", lightId: 1 },
    bulb2: { driver: "hue-light", lightId: 2 },
    bulb3: { driver: "hue-light", lightId: 3 },
    bulb4: { driver: "hue-light", lightId: 4 },
    bulb5: { driver: "hue-light", lightId: 5 },
    bulb6: { driver: "hue-light", lightId: 8 },
    bulb7: { driver: "hue-light", lightId: 9 }
  },

  work: function(my) {
    for (var d in my.devices) {
      my.devices[d].turnOff();
    }
  }
}).start();