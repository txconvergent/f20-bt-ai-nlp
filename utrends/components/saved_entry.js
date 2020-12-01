import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export class SavedEntry extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            text: props.text,
            source: props.text,
        }
    }

    render() {
        return (
            <View style={styles.container}>
                <Text style={styles.sourceText}>{this.state.source}</Text>
                <Text style={styles.bodyText}>{this.state.text}</Text>
            </View>
        )
    }
}

const styles = StyleSheet.create({

    container: {
        backgroundColor: '#19297C',
        height: 100,
        marginBottom: 10,
        paddingLeft: 10,
        paddingTop: 10,
        borderRadius: 10,
    },

    bodyText: {
        fontSize: 15,
        fontFamily: 'Avenir',
        color: 'white',
    },

    sourceText: {
        fontSize: 15,
        fontFamily: 'AvenirNext-Bold',
        color: 'white'
    }

});
