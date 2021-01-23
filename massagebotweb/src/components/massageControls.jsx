import React, { Component } from "react";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Button from "@material-ui/core/Button";

class MassageControls extends Component {
  state = { force: 0.66, speed: 0.66, running: false };

  handleForce = (event) => {
    this.setState({ force: event.target.value });
  };
  handleSpeed = (event) => {
    this.setState({ speed: event.target.value });
  };

  render() {
    return (
      <div style={{ width: 100 + "%" }}>
        <FormControl style={{ width: 90 + "%", padding: 1 + "%" }}>
          <InputLabel>Speed</InputLabel>
          <Select value={this.state.speed} onChange={this.handleSpeed}>
            <MenuItem value={0.333}>Slow</MenuItem>
            <MenuItem value={0.66}>Medium</MenuItem>
            <MenuItem value={1.0}>Fast</MenuItem>
          </Select>
        </FormControl>
        <br />
        <FormControl style={{ width: 90 + "%", padding: 1 + "%" }}>
          <InputLabel>Force</InputLabel>
          <Select value={this.state.force} onChange={this.handleForce}>
            <MenuItem value={0.333}>Low</MenuItem>
            <MenuItem value={0.66}>Medium</MenuItem>
            <MenuItem value={1.0}>High</MenuItem>
          </Select>
        </FormControl>
        <Button
          variant="contained"
          style={{
            width: 90 + "%",
            padding: 1 + "%",
            backgroundColor: "#4caf50",
          }}
        >
          Start
        </Button>
        <Button
          variant="contained"
          style={{
            width: 90 + "%",
            padding: 1 + "%",
            backgroundColor: "#f44336",
          }}
        >
          Stop
        </Button>
      </div>
    );
  }
}

export default MassageControls;
