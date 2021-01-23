import React, { Component } from "react";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Checkbox from "@material-ui/core/Checkbox";
import Select from "@material-ui/core/Select";
import Button from "@material-ui/core/Button";

class MassageControls extends Component {
  state = {
    force: 0.66,
    speed: 0.66,
    running: false,
    upper: true,
    mid: true,
    lower: true,
  };

  sendState = () => {
    var fetch_url = window.location.href;
    fetch_url = "http://192.168.2.104:5000/settings";
    fetch_url = fetch_url.concat("?force=" + this.state.force);
    fetch_url = fetch_url.concat("&speed=" + this.state.speed);
    fetch_url = fetch_url.concat("&state=" + this.state.running);
    fetch_url = fetch_url.concat("&upper=" + this.state.upper);
    fetch_url = fetch_url.concat("&mid=" + this.state.mid);
    fetch_url = fetch_url.concat("&lower=" + this.state.lower);
    fetch(fetch_url);
  };

  componentDidMount() {
    this.sendState();
  }

  handleForce = (event) => {
    this.setState({ force: event.target.value }, () => this.sendState());
  };
  handleSpeed = (event) => {
    this.setState({ speed: event.target.value }, () => this.sendState());
  };

  handleUpper = (event) => {
    this.setState({ upper: event.target.checked }, () => this.sendState());
  };

  handleMid = (event) => {
    this.setState({ mid: event.target.checked }, () => this.sendState());
  };
  handleLower = (event) => {
    this.setState({ lower: event.target.checked }, () => this.sendState());
  };

  handleStart = () => {
    this.setState({ running: true }, () => this.sendState());
  };
  handleStop = () => {
    this.setState({ running: false }, () => this.sendState());
  };

  render() {
    return (
      <div style={{ width: 100 + "%" }}>
        <br />
        <br />
        <FormControl style={{ width: 90 + "%", padding: 1 + "%" }}>
          <InputLabel>Speed</InputLabel>
          <Select value={this.state.speed} onChange={this.handleSpeed}>
            <MenuItem value={0.333}>Slow</MenuItem>
            <MenuItem value={0.66}>Medium</MenuItem>
            <MenuItem value={1.0}>Fast</MenuItem>
          </Select>
        </FormControl>
        <br />
        <br />
        <FormControl style={{ width: 90 + "%", padding: 1 + "%" }}>
          <InputLabel>Force</InputLabel>
          <Select value={this.state.force} onChange={this.handleForce}>
            <MenuItem value={0.333}>Low</MenuItem>
            <MenuItem value={0.66}>Medium</MenuItem>
            <MenuItem value={1.0}>High</MenuItem>
          </Select>
        </FormControl>
        <br />
        <br />
        <FormControl>
          Upper (Trapezius)
          <Checkbox
            checked={this.state.upper}
            name="upperCheck"
            onChange={this.handleUpper}
            color="primary"
          />
        </FormControl>
        <br />
        <FormControl>
          Mid (Latissimus)
          <Checkbox
            checked={this.state.mid}
            name="midCheck"
            onChange={this.handleMid}
            color="primary"
          />
        </FormControl>
        <br />
        <FormControl>
          Lower (Erector)
          <Checkbox
            checked={this.state.lower}
            name="LowerCheck"
            onChange={this.handleLower}
            color="primary"
          />
        </FormControl>
        <br />
        <br />
        <Button
          onClick={this.handleStart}
          variant="contained"
          style={{
            width: 90 + "%",
            padding: 1 + "%",
            backgroundColor: "#4caf50",
          }}
        >
          Start
        </Button>
        <br />
        <br />
        <Button
          onClick={this.handleStop}
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
