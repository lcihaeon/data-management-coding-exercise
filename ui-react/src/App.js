import React, { Component, Fragment } from "react";
import DrawerAppBar from "./components/drawer-app-bar";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import ManageServices from "./pages/manage-services";
import UploadFiles from "./pages/upload-files";
import MyGithub from "./pages/my-github";

class App extends Component {
  render() {
    return (
        <BrowserRouter>
          <Fragment>
            <DrawerAppBar />
            <Routes>
              <Route exact path="/manage-services" element={<ManageServices/>}/>
              <Route exact path="/upload-files" element={<UploadFiles/>}/>
              <Route path="/github" element={<MyGithub/>}/>
              <Route path="/" element={<ManageServices/>}/>
            </Routes>
          </Fragment>
        </BrowserRouter>
    );
  }
}

export default App;
