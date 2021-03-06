import React from "react";
import makeStyles from "@material-ui/core/styles/makeStyles";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import TopicsTreeSelect from "./TopicsTreeSelect";

export default function Step2(props) {

  const useStyles = makeStyles((theme) => ({
    topics: {
      marginLeft: 'auto',
      marginRight: 'auto',
      textAlign: 'center'
    },
    topicsTree: {
      marginTop: theme.spacing(1),
    }
  }));

  const classes = useStyles();

  return (
    <>
      <CardHeader className={"stepHeader"}
                  title={props.title}
                  avatar={
                    <Avatar aria-label="step2">2</Avatar>
                  }
                  action={
                    <IconButton
                      aria-describedby={'settings-popover'}
                    >&nbsp;&nbsp;&nbsp;</IconButton>
                  }
      />
      <p className={"stepSubHeader"}>Select Data Commons variables to retrieve values from</p>
      <CardContent>
        <div className={classes.topics}>

          <div className={classes.topicsTree}>

            <TopicsTreeSelect
              setDcVariableNames={props.setDcVariableNames}
              showDcVariableNamesError={props.showDcVariableNamesError}
              validateStep2DcVariableNames={props.validateStep2DcVariableNames}/>
          </div>
        </div>
      </CardContent>
    </>
  );
}