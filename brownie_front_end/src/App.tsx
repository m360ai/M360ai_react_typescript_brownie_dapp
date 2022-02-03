import React from 'react';
import './App.css';
import { DAppProvider, ChainId } from '@usedapp/core'
import { Header } from "./components/Header"


function App() {
  return (
    <DAppProvider config={{
      supportedChains: [ChainId.Kovan, ChainId.Rinkeby]
    }}>
      <div className="App-Header">
        Welcome to the Decentralized World</div> <Header />
    </DAppProvider >

  );
}

export default App;
