$(function () {
    var loadAndRun = function () {
        var templates = {},
 
            views = {},
 
            runApp = function () {
                var List = Backbone.View.extend({
                        events: {
                            'click .ui-widget-content': 'handleClick'
                    },
                    handleClick: function (event) {
                         event.preventDefault();
                         if ($(event.target).attr('href') !== undefined) {
                            Backbone.history.navigate('edit/1', true);
                        }
                    },
                    initialize: function () {
                        _(this).bindAll('handleClick', 'render');
                    },
                    render: function () {
                        $(this.el).html(Mustache.to_html(templates.items, views.items));
                    }
                }),
 
                Edit = Backbone.View.extend({
                    events: {
                        'click a': 'handleClick'
                    },
                    handleClick: function (event) {
                         event.preventDefault();
                         if ($(event.target).attr('href') !== undefined) {
                            Backbone.history.navigate('items', true);
                         }
                     },
                    initialize: function () {
                        _(this).bindAll('handleClick', 'render');
                    },
                    render: function () {
                        $(this.el).html(Mustache.to_html(templates.edit, views.edit));
                        this.delegateEvents();
                    }
                }),
 
                Router = Backbone.Router.extend({
                    routes: {
                        'items': 'list',
                        'edit/:id': 'details',
                    },
                    list: function () {
                        var view = new List({
							el: $('#content')
                        });
                        view.render();
                    },
                    details: function (id) {
                         var view = new Edit({
							 el: $('#content')
                         });
                         view.render();
                     }
                });
 
            new Router();
 
            Backbone.history.start({
                pushState: true
            });
        };
 
        views.items = {
                items: [{id: '1', 'item': 'Joe'},{id: '2', 'item': 'Victoria'}]
            };
 
        views.edit = {
            item: 'Joe'
        }
 
        $.get('/ajax/items', null, function (data) {
            templates.items = data;
 
            $.get('/ajax/edit', null, function (data) {
                templates.edit = data;
 
                runApp();
            });
        });
    };
 
    if (Modernizr.history) {
        loadAndRun();
    }
});