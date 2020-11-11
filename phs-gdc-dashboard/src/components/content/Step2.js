import React from "react";
import makeStyles from "@material-ui/core/styles/makeStyles";

export default function Step1(props) {

  const useStyles = makeStyles((theme) => ({}));

  const classes = useStyles();
  const [topic, setTopic] = React.useState('');

  const handleChange = (event) => {
    setTopic(event.target.value);
  };

  return (
    <div>
      <h2>{props.title}</h2>
      <h4>Enter or select the variables (topics) for which you want to retrieve contextual values</h4>
    </div>
  );
}