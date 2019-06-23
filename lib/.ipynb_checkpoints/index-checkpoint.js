"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const mainmenu_1 = require("@jupyterlab/mainmenu");
const apputils_1 = require("@jupyterlab/apputils");
const widgets_1 = require("@phosphor/widgets");
require("../style/index.css");
/**
 * Initialization data for the jupyterlab_myext extension.
 */
const extension = {
    id: 'snippets',
    autoStart: true,
    requires: [mainmenu_1.IMainMenu, apputils_1.ICommandPalette],
    activate: activate_custom_menu
};
exports.default = extension;
exports.BookMarks = [
    {
        name: 'gmo',
        url: 'https://www.gmo.jp/en/',
        description: 'Creating a simple JupyterLab plugin adding BookMark menu',
        target: 'widget'
    }
];
function activate_custom_menu(app, mainMenu, palette) {
    // create new commands and add them to app.commands
    function appendNewCommand(item) {
        let iframe = null;
        let command = `BookMark-${item.name}:show`;
        app.commands.addCommand(command, {
            label: item.name,
            execute: () => {
                if (item.target == '_blank') {
                    let win = window.open(item.url, '_blank');
                    win.focus();
                }
                else if (item.target == 'widget') {
                    if (!iframe) {
                        iframe = new apputils_1.IFrame();
                        iframe.url = item.url;
                        iframe.id = item.name;
                        iframe.title.label = item.name;
                        iframe.title.closable = true;
                        iframe.node.style.overflowY = 'auto';
                    }
                    if (iframe == null || !iframe.isAttached) {
                        app.shell.addToMainArea(iframe);
                        app.shell.activateById(iframe.id);
                    }
                    else {
                        app.shell.activateById(iframe.id);
                    }
                }
            }
        });
    }
    exports.BookMarks.forEach(item => appendNewCommand(item));
    // add to mainMenu
    let menu = Private.createMenu(app);
    mainMenu.addMenu(menu, { rank: 80 });
    return Promise.resolve(void 0);
}
exports.activate_custom_menu = activate_custom_menu;
/**
 * A namespace for help plugin private functions.
 */
var Private;
(function (Private) {
    /**
     * Creates a menu for the help plugin.
     */
    function createMenu(app) {
        const { commands } = app;
        let menu = new widgets_1.Menu({ commands });
        menu.title.label = 'snippets';
        exports.BookMarks.forEach(item => menu.addItem({ command: `BookMark-${item.name}:show` }));
        return menu;
    }
    Private.createMenu = createMenu;
})(Private || (Private = {}));
