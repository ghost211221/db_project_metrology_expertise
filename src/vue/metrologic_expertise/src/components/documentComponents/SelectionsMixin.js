export const SelectionsMixin = {
  data () {
    return {
      firstEl: '',
      secondEl: '',
      selectedRange: null,
      range: null
    }
  },
  methods: {
    onmousedown (event) {
      this.firstEl = event.target.className
    },
    onmouseup (event) {
      this.secondEl = event.target.className
      this.$emit('textSelected', window.getSelection().toString(), true)
      // this.highlight()
    },
    getSelectedRange () {
      if (window.getSelection) {
        const sel = window.getSelection()
        if (sel.getRangeAt && sel.rangeCount) {
          this.selectedRange = sel.getRangeAt(0)
        }
      } else if (document.selection) {
        this.selectedRange = document.selection.createRange()
      }
    },
    surroundSelection () {
      const span = document.createElement('span')
      span.className = 'highlight'
      span.style.backgroundColor = '#D05555'
      if (window.getSelection) {
        var sel = window.getSelection()
        if (sel.rangeCount) {
          var range = this.selectedRange.cloneRange()
          range.surroundContents(span)
          sel.removeAllRanges()
          sel.addRange(range)
        }
      }
    },
    highlight () {
      this.getSelectedRange()
      console.log(this.selectedRange)
      console.log(this.highlightAllow)
      if (this.selectedRange && this.highlightAllow) {
        this.surroundSelection()
        this.$emit('textHighlighted')
      }
    }
  },
  watch: {
    highlightAllow: function () {
      if (this.highlightAllow) {
        this.highlight()
      }
    },
  }
}
