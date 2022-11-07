// TODO: remove import *
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import GitHubIcon from '@mui/icons-material/GitHub';

export default function MyGithub() {
    return (
        <React.Fragment>
            <CssBaseline/>
            <Container maxWidth="lg">
                {/*<Box sx={{bgcolor: '#cfe8fc', height: '100vh'}}>*/}
                <Box sx={{ height: '100vh'}}>
                    <GitHubIcon/> GitHub Repo: https://github.com/lcihaeon/grace-liao-coding-exercise
                </Box>
            </Container>
        </React.Fragment>
    );
}
