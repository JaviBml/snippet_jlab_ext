import { JupyterLab, JupyterLabPlugin } from '@jupyterlab/application';
import { IMainMenu } from '@jupyterlab/mainmenu';
import { ICommandPalette } from '@jupyterlab/apputils';
import '../style/index.css';
/**
 * Initialization data for the jupyterlab_myext extension.
 */
declare const extension: JupyterLabPlugin<void>;
export default extension;
export declare const BookMarks: {
    name: string;
    url: string;
    description: string;
    target: string;
}[];
export declare function activate_custom_menu(app: JupyterLab, mainMenu: IMainMenu, palette: ICommandPalette): Promise<void>;
