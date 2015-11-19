angular.module('webz', ['ui.router', 'ui.bootstrap'])

.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to the home state at /
  $urlRouterProvider.otherwise("/");
  //
  // Now set up the states
  $stateProvider
    .state('home', {
      url: "/",
      controller: 'CountCtrl as vm',
      templateUrl: "/static/home.html"
    });
})
.controller('CountCtrl', function CountCtrl() {
  this.count = 4;
})
.component('counter', {
  bindings: {
    count: '='
  },
  controller: function () {
    function increment() {
      this.count++;
    }
    function decrement() {
      this.count--;
    }
    this.increment = increment;
    this.decrement = decrement;
  },
  template: [
    '<div class="todo">',
      '<input type="text" ng-model="counter.count">',
      '<button type="button" ng-click="counter.decrement();">-</button>',
      '<button type="button" ng-click="counter.increment();">+</button>',
    '</div>'
  ].join('')
});
