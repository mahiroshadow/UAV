import { app, BrowserWindow } from 'electron'
import path from 'path'

let win: BrowserWindow | null

const createWindow = () => {
  win = new BrowserWindow({
    webPreferences: {
      devTools: true,
      nodeIntegration: true,
      contextIsolation: false,
    },
  })

  win.loadURL(`http://127.0.0.1:8270/`)
}

app.whenReady().then(createWindow)
