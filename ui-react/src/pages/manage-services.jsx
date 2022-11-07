import React from 'react';
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import {Stack, Switch} from "@mui/material";
import Typography from "@mui/material/Typography";

class ManageServices extends React.Component {
    render() {
        return (
            <React.Fragment>
                <CssBaseline/>
                <Container maxWidth="lg">
                    <Box sx={{height: '100vh'}}>
                        <h2>Manage Services</h2>
                        <Stack direction="row" spacing={1} alignItems="center">
                            <Typography style={{ paddingRight: '50px' }}>File Watcher Service</Typography>
                            <Typography>Off</Typography>
                            {/*<Switch defaultChecked />*/}
                            <Switch />
                            <Typography>On</Typography>
                        </Stack>
                    </Box>
                </Container>
            </React.Fragment>
        )
    }
}

export default ManageServices
