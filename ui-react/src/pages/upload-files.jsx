import React from 'react';
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";

class UploadFiles extends React.Component {
    render() {
        return (
            <React.Fragment>
                <CssBaseline/>
                <Container maxWidth="lg">
                    <Box sx={{height: '100vh'}}>
                        <h2>Upload Files</h2>
                        <Button variant="contained">UPLOAD </Button>
                    </Box>
                </Container>
            </React.Fragment>
        )
    }
}

export default UploadFiles

